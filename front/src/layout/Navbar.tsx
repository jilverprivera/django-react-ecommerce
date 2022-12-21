import { useLocation, Link } from "react-router-dom";
import { BsSearch, BsHeart, BsBag } from "react-icons/bs";

import ROUTES from "../data/routes.json";
import NavbarBtnDrawer from "./NavbarBtnDrawer";
import { useContext } from "react";
import { Context } from "../context";

const Navbar = () => {
  const { pathname } = useLocation();
  const { setSearchModal, searchModal } = useContext(Context);

  return (
    <header className='w-full'>
      <nav className='w-11/12 mx-auto h-20 flex items-center justify-between'>
        <div className='flex items-center justify-center'>
          {ROUTES.map((route, i) => (
            <Link
              to={route.route}
              key={i}
              className={`${
                pathname === route.route
                  ? "text-zinc-900 font-medium"
                  : "text-zinc-700 font-light"
              } text-base mx-4 first:ml-0 tracking-wider`}
            >
              {route.name}
            </Link>
          ))}
        </div>
        <div className='flex items-center justify-center'>
          <button
            className='flex items-center justify-center mx-3'
            onClick={() => setSearchModal(!searchModal)}
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
    </header>
  );
};

export default Navbar;
