import { useContext } from "react";
import { Link } from "react-router-dom";
import { BsSearch, BsHeart, BsBag } from "react-icons/bs";
import { AnimatePresence, motion } from "framer-motion";
import { LayoutContext } from "../context/LayoutContext";
import NavbarBtnDrawer from "./NavbarBtnDrawer";
import FlyoutButton from "./FlyoutButton";

const Navbar = () => {
  const { openSearch, setOpenSearch, openFlyout } = useContext(LayoutContext);

  return (
    <header className='fixed top-0 left-0 w-full z-50'>
      <nav className='h-24 w-11/12 mx-auto  flex items-center justify-between z-50 '>
        <div className='flex items-center justify-center'>
          <Link to='/' className={`text-3xl mr-6 font-bold`}>
            LOGO
          </Link>
          <FlyoutButton text='Categories' />
        </div>
        <div className='flex items-center justify-center'>
          <button
            className='flex items-center justify-center mx-3'
            onClick={() => setOpenSearch(!openSearch)}
          >
            <span className='text-sm'>
              <BsSearch />
            </span>
            <span className='mx-1.5 tracking-wide font-normal'>Search</span>
          </button>
          <Link
            to='/wishlist'
            className='flex items-center justify-center mx-3'
          >
            <span className='text-sm'>
              <BsHeart />
            </span>
            <span className='mx-1.5 tracking-wide font-normal'>Wish List</span>
            {/* <span className='text-sm'>({cart.length})</span> */}
          </Link>
          <Link
            to='/cart'
            className='flex items-center justify-center ml-3 mr-6'
          >
            <span className='text-sm'>
              <BsBag />
            </span>
            <span className='mx-1.5 tracking-wide font-normal'>Cart</span>
            {/* <span className='text-sm'>({wishList.length})</span> */}
          </Link>

          <NavbarBtnDrawer />
        </div>
      </nav>
      <AnimatePresence exitBeforeEnter initial={false}>
        {openFlyout && (
          <motion.div
            initial={{ opacity: 0, y: -5, height: 0 }}
            animate={{ opacity: 1, y: 0, height: "24rem" }}
            exit={{ opacity: 0, y: -5, height: 0 }}
            transition={{ duration: 0.25 }}
            className='fixed top-24 left-0 w-full bg-white rounded-b-xl flex items-center justify-center shadow-md'
          >
            <div className='w-11/12 mx-auto'>Testing Flyout</div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
};

export default Navbar;
