import { useContext } from "react";
import { Link } from "react-router-dom";
import { AnimatePresence } from "framer-motion";

import UpperNavbar from "./UpperNavbar";
import LowerNavbar from "./LowerNavbar";
import CategoriesFlyout from "./CategoriesFlyout";
import { LayoutContext } from "../context/LayoutContext";

import ICON from "../assets/icon.svg";
import { useWindow } from "../hooks/useWindow";

const Navbar = () => {
  const { openFlyout, setOpenFlyout } = useContext(LayoutContext);
  const { scrollY } = useWindow();
  return (
    <header
      className={`${
        openFlyout || scrollY > 80 ? "bg-white" : "bg-transparent"
      } fixed top-0 left-0 w-full z-50 duration-200`}
    >
      <UpperNavbar />
      <nav className='h-20 max-w-screen-2xl w-11/12 mx-auto flex items-center justify-between z-50 relative '>
        <Link
          to='/'
          className={`absolute top-2/4 left-2/4 -translate-y-2/4 -translate-x-2/4 text-3xl mr-6 font-bold`}
          onClick={() => setOpenFlyout(false)}
        >
          <img src={ICON} alt='icon' />
        </Link>
      </nav>
      <LowerNavbar />
      <AnimatePresence initial={false}>
        {openFlyout && <CategoriesFlyout />}
      </AnimatePresence>
    </header>
  );
};

export default Navbar;
