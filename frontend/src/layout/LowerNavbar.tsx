import { useContext } from "react";
import { Link } from "react-router-dom";
import { LayoutContext } from "../context/LayoutContext";
import FlyoutButton from "./FlyoutButton";

const LowerNavbar = () => {
  const { setOpenFlyout } = useContext(LayoutContext);

  return (
    <div className='w-full h-16 flex items-center justify-center'>
      <Link
        to='/'
        className={`text-base mr-6 font-normal`}
        onClick={() => setOpenFlyout(false)}
      >
        Home
      </Link>
      <FlyoutButton text='Categories' />
      <Link
        to='/shop'
        className={`text-base mr-6 font-normal`}
        onClick={() => setOpenFlyout(false)}
      >
        Shop
      </Link>
      <Link
        to='/about'
        className={`text-base mr-6 font-normal`}
        onClick={() => setOpenFlyout(false)}
      >
        About
      </Link>
      <Link
        to='/'
        className={`text-base mr-6 font-normal`}
        onClick={() => setOpenFlyout(false)}
      >
        Wishlist
      </Link>
      <Link
        to='/'
        className={`text-sm mr-6 font-normal`}
        onClick={() => setOpenFlyout(false)}
      >
        Cart
      </Link>
    </div>
  );
};

export default LowerNavbar;
