import { useContext } from "react";
import { MdOutlineKeyboardArrowDown } from "react-icons/md";
import { LayoutContext } from "../context/LayoutContext";

type props = {
  text: string;
};

const FlyoutButton = ({ text }: props) => {
  const { openFlyout, setOpenFlyout } = useContext(LayoutContext);

  return (
    <button
      className='mx-3 flex items-center justify-center'
      onClick={() => setOpenFlyout(!openFlyout)}
    >
      <span className='mr-1.5'>{text}</span>
      <span>
        <MdOutlineKeyboardArrowDown />
      </span>
    </button>
  );
};

export default FlyoutButton;
