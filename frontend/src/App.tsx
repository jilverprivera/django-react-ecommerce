import { useEffect, useState } from "react";
import { BsFillStarFill } from "react-icons/bs";
import Navbar from "./layout/Navbar";
import AppRouter from "./routes/AppRouter";
import { ProductTypes } from "./types";
import { category } from "./types/categories";

const App = () => {
  const [categories, setCategories] = useState<category[]>([]);
  const [products, setProducts] = useState<ProductTypes[]>([]);
  useEffect(() => {
    const getCategories = async () => {
      const response = await fetch("http://127.0.0.1:8000/api/categories/");
      const data = await response.json();
      console.log(data);
      setCategories(data);
    };
    getCategories();
  }, []);
  useEffect(() => {
    const getCategories = async () => {
      const response = await fetch("http://127.0.0.1:8000/api/products/");
      const data = await response.json();
      console.log(data);
      setProducts(data);
    };
    getCategories();
  }, []);

  return (
    <>
      <Navbar />
      <main className="w-full">
        <AppRouter />
      </main>
    </>
  );
};

export default App;
