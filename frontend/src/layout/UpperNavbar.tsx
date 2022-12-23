import { useContext } from "react";
import { TfiUser, TfiWorld } from "react-icons/tfi";
import { Link } from "react-router-dom";
import { LayoutContext } from "../context/LayoutContext";
import { networks } from "../data/networks";

const UpperNavbar = () => {
  const { setOpenFlyout } = useContext(LayoutContext);

  return (
    <div className='w-full bg-stone-300'>
      <div className='h-12 max-w-screen-2xl w-11/12 mx-auto flex items-center justify-between z-50'>
        <div className='flex items-center justify-center'>
          {networks.map((network, i) => (
            <a
              href={network.url}
              target='_blank'
              rel='noreferrer noopener'
              className='first:ml-0 last:mr-0 mx-1.5 text-base text-zinc-700'
            >
              {network.icon}
            </a>
          ))}
        </div>
        <div className='flex items-center justify-center'>
          <Link
            to='/customer-service'
            className='flex items-center justify-center mr-3'
            onClick={() => setOpenFlyout(false)}
          >
            <span className='text-xs'>
              <TfiWorld />
            </span>
            <span className='mx-1.5 text-sm font-normal'>Customer service</span>
          </Link>
          <Link
            to='/signin'
            className='flex items-center justify-center'
            onClick={() => setOpenFlyout(false)}
          >
            <span className='text-xs'>
              <TfiUser />
            </span>
            <span className='mx-1.5 text-sm font-normal'>Sign in</span>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default UpperNavbar;
