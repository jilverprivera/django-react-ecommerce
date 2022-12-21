import { AnimatePresence } from "framer-motion";
import { Routes, Route, useLocation } from "react-router-dom";

import About from "../pages/About";
import Cart from "../pages/Cart";
import Categories from "../pages/Categories";
import Contact from "../pages/Contact";
import Home from "../pages/Home";
import Shop from "../pages/Shop";
import Wishlist from "../pages/Wishlist";

const AppRouter = () => {
  const location = useLocation();

  return (
    <AnimatePresence exitBeforeEnter initial={false}>
      <Routes location={location} key={location.pathname}>
        <Route path='/' element={<Home />} />
        <Route path='/shop' element={<Shop />} />
        <Route path='/categories' element={<Categories />} />
        <Route path='/about' element={<About />} />
        <Route path='/contact' element={<Contact />} />
        <Route path='/cart' element={<Cart />} />
        <Route path='/wishlist' element={<Wishlist />} />
      </Routes>
    </AnimatePresence>
  );
};

export default AppRouter;
