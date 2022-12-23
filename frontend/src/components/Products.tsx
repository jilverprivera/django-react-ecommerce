import React from "react";
import { useData } from "../hooks/useData";
import { ProductTypes } from "../types";
import ProductCard from "./ProductCard";

const Products = () => {
  const { data, isLoading } = useData("http://127.0.0.1:8000/api/products/");
  return (
    <section className='w-full mx-auto grid grid-cols-3 gap-6'>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        data.map((item: ProductTypes) => <ProductCard {...item} />)
      )}
    </section>
  );
};

export default Products;
