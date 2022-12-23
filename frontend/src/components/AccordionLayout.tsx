import {
  MdOutlineKeyboardArrowDown,
  MdOutlineKeyboardArrowUp,
} from "react-icons/md";
import { AnimatePresence, motion } from "framer-motion";
import { CategoryTypes } from "../types";
import AccordionContent from "./AccordionContent";

type props = {
  category: CategoryTypes;
  activeCategory: number | null;
  setActiveCategory: (arg: number | null) => void;
};
const Accordion = ({ category, activeCategory, setActiveCategory }: props) => {
  return (
    <div className='w-full'>
      <div
        className='w-full flex items-start justify-between border-b-2 p-3'
        onClick={() => setActiveCategory(category.id)}
      >
        <p>{category.name}</p>
        <div className='flex items-center justify-center'>
          <span
            className={`${
              activeCategory === category.id ? "rotate-0" : "rotate-180"
            } 'w-6 h-6 text-xl`}
          >
            <MdOutlineKeyboardArrowUp />
          </span>
        </div>
      </div>
      <AnimatePresence exitBeforeEnter>
        {activeCategory === category.id && (
          <AccordionContent activeCategory={activeCategory} />
        )}
      </AnimatePresence>
    </div>
  );
};

export default Accordion;
