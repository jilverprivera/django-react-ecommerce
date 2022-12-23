import { motion } from "framer-motion";
import { useData } from "../hooks/useData";
import { SubCategoryTypes } from "../types";

type props = {
  activeCategory: number;
};
const AccordionContent = ({ activeCategory }: props) => {
  const { data, isLoading } = useData(
    `http://127.0.0.1:8000/api/sub_categories/${activeCategory}/`
  );
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className='px-6 py-3'
    >
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <div>
          {data.map((subcategory: SubCategoryTypes) => (
            <p key={subcategory.id} className='py-1.5 last:pb-0'>
              {subcategory.name}
            </p>
          ))}
        </div>
      )}
    </motion.div>
  );
};

export default AccordionContent;
