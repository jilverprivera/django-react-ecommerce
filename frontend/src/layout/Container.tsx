import { useContext } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { LayoutContext } from "../context/LayoutContext";
import SearchModal from "./SearchModal";
import { layout } from "../types/layout";

const Container = ({ children, title }: layout) => {
  document.title = title;
  const { openSearch } = useContext(LayoutContext);

  return (
    <>
      <motion.main
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: 10 }}
        transition={{ duration: 0.25 }}
        className='mx-auto w-full bg-white'
      >
        {children}
      </motion.main>
      <AnimatePresence exitBeforeEnter initial={false}>
        {openSearch && <SearchModal />}
      </AnimatePresence>
    </>
  );
};

export default Container;
