import { useLocation } from "react-router-dom";
import { AnimatePresence, motion } from "framer-motion";

import { layout } from "../types/layout";
import SearchModal from "./SearchModal";
import { useContext } from "react";
import { Context } from "../context";

const Container = ({ children, title }: layout) => {
  document.title = title;
  const { searchModal } = useContext(Context);

  return (
    <>
      <motion.main
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: 10 }}
        transition={{ duration: 0.25 }}
        className='mx-auto w-full bg-white pt-24'
      >
        {children}
      </motion.main>
      <AnimatePresence exitBeforeEnter initial={false}>
        {searchModal && <SearchModal />}
      </AnimatePresence>
    </>
  );
};

export default Container;
