import '../styles/DisplayProducts.css'
import ProductCard from './ProductCard';
const DisplayProducts = ({query , products}) => {

return (
    <div className='page'>
    <h2>Results for {query[0].toUpperCase() + query.slice(1)}</h2>
    <div className='product-container'>
        {products.map((product) => (
            <ProductCard key={product.title} product={product} />
        
        ))}
    </div>
  </div>  
  );
}

export default DisplayProducts