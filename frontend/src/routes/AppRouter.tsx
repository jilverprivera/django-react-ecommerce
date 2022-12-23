import { AnimatePresence } from "framer-motion";
import { Routes, Route, useLocation } from "react-router-dom";

import About from "../pages/About";
import SignIn from "../pages/auth/signin";
import Cart from "../pages/Cart";
import Categories from "../pages/Categories";
import Contact from "../pages/Contact";
import CustomerService from "../pages/customer-service/Index";
import Home from "../pages/Home";
import Shop from "../pages/Shop";
import Wishlist from "../pages/Wishlist";
import { PublicRoute } from "./PublicRoute";

const AppRouter = () => {
  const location = useLocation();

  return (
    <AnimatePresence exitBeforeEnter initial={false}>
      <Routes location={location} key={location.pathname}>
        {/* Base URLS */}
        <Route path='/' element={<Home />} />
        <Route path='/customer-service' element={<CustomerService />} />
        <Route path='/about' element={<About />} />
        <Route path='/contact' element={<Contact />} />
        <Route path='/categories' element={<Categories />} />
        <Route path='/shop' element={<Shop />} />
        {/* Private URLS */}
        <Route path='/cart' element={<Cart />} />
        <Route path='/wishlist' element={<Wishlist />} />
        {/* Public URLS */}
        <Route path='/signin' element={<PublicRoute component={SignIn} />} />
        <Route path='/signup' element={<PublicRoute component={SignIn} />} />
      </Routes>
    </AnimatePresence>
  );
};

export default AppRouter;
