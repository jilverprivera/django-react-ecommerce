import { useContext } from "react";
import { motion } from "framer-motion";
import { LayoutContext } from "../context/LayoutContext";
import { useData } from "../hooks/useData";
import { SubCategoryTypes } from "../types";

const SubCategoryList = () => {
  const { categorySearch } = useContext(LayoutContext);

  const { data } = useData(
    `http://127.0.0.1:8000/api/sub_categories/${categorySearch}/`
  );
  return (
    <motion.ul
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      {data &&
        data.map((category: SubCategoryTypes) => (
          <motion.li
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className='my-3 text-base'
            key={category.id}
          >
            {category.name}
          </motion.li>
        ))}
    </motion.ul>
  );
};

export default SubCategoryList;
