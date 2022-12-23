import { useContext } from "react";
import { motion } from "framer-motion";
import CategoryList from "../components/CategoryList";
import SubCategoryList from "../components/SubCategoryList";
import { LayoutContext } from "../context/LayoutContext";

const CategoriesFlyout = () => {
  const { categorySearch } = useContext(LayoutContext);

  return (
    <motion.div
      initial={{ opacity: 0, y: -5, height: 0 }}
      animate={{ opacity: 1, y: 0, height: "24rem" }}
      exit={{ opacity: 0, y: -5, height: 0 }}
      transition={{ duration: 0.25 }}
      className='fixed top-48 left-0 w-full bg-white rounded-b-xl  shadow-md py-6'
    >
      <div className='max-w-screen-2xl w-11/12 mx-auto grid grid-cols-4 gap-12'>
        <div className='w-full'>
          <p className='text-xl font-semibold mb-6'>Categories</p>
          <CategoryList />
        </div>
        {categorySearch !== null && (
          <div className='w-full'>
            <div>
              <p className='text-xl font-semibold mb-6'>Sub Categories</p>
              <SubCategoryList />
            </div>
          </div>
        )}
      </div>
    </motion.div>
  );
};

export default CategoriesFlyout;
