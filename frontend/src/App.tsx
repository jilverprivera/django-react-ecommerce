import Navbar from "./layout/Navbar";
import AppRouter from "./routes/AppRouter";

const App = () => {
  // useEffect(() => {
  //   const getCategories = async () => {
  //     const response = await fetch("http://127.0.0.1:8000/api/products/");
  //     const data = await response.json();
  //     console.log(data);
  //     setProducts(data);
  //   };
  //   getCategories();
  // }, []);

  return (
    <>
      <Navbar />
      <main className='w-full'>
        <AppRouter />
      </main>
    </>
  );
};

export default App;
