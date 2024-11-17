import "./App.css";
import * as data from '../../user_queries.json';
import {useState , useEffect} from "react";
import DisplayProducts from "./components/DisplayProducts";

function App() {
  const [query, setQuery] = useState("headphones");
  const [loading, setLoading] = useState(false);
  const [products, setProducts] = useState([]);

  const runQuery = async (query)=>{
    if (!query) {
      alert("Please enter a search query.");
      return;
    }
    
    try {
          setLoading(true);
          const response = await fetch('http://localhost:5000/scrape', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ query }),
          });

          if (!response.ok) {
              throw new Error("Failed to fetch data");
          }

          const data = await response.json();
          setProducts(data);
      } catch (error) {
          console.error("Error fetching data:", error);
          alert("Error fetching data. Check the console for more details.");
      }
      finally {
        setLoading(false); 
    }
  }
  
  const onCategoryChange = (e)=>{
    setProducts([])
    setQuery(e.target.value) ;
  }
  useEffect( () => {
     runQuery(query)
  }, [query]);

  return (
    <div className="App">

      <h1>Amazon Product Scraper</h1>
      <label htmlFor="query">Choose a Category </label>
      <select name="query" id="query" onChange={onCategoryChange}>
        {
            data.default.map((option)=>{return (<option key={option} value={option}>{option[0].toUpperCase() + option.slice(1)}</option>)})
        }
      </select>
      {loading && <div  className="loader"/>}
      {!loading && products.length > 0 &&  <DisplayProducts query={query} products={products}/>}
     
    </div>
  );
}

export default App;
