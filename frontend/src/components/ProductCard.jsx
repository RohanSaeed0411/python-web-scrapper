import React from 'react';
import '../styles/ProductCard.css';

const ProductCard = ({ product }) => {
    return (
        <div className="product-card">
            <img
                src={product.image_url}
                alt={product.title}
                className="product-card-image"
            />
            <div className="product-card-details">
                <h3 className="product-card-title">{product.title}</h3>
                <p className="product-card-reviews">
                    <strong>Reviews:</strong> {product.total_reviews}
                </p>
                <p className="product-card-price">
                    <strong>Price:</strong> {product.price}
                </p>
            </div>
        </div>
    );
};

export default ProductCard;
