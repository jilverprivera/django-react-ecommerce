import { useContext } from "react";
import { BsSearch } from "react-icons/bs";
import { MdClose } from "react-icons/md";
import { motion } from "framer-motion";
import { LayoutContext } from "../context/LayoutContext";
import { useData } from "../hooks/useData";
import { CategoryTypes } from "../types";

const SearchModal = () => {
  const { setOpenSearch } = useContext(LayoutContext);
  const { data, isLoading } = useData("http://127.0.0.1:8000/api/categories/");

  return (
    <motion.div
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -10 }}
      transition={{ duration: 0.25 }}
      className='fixed top-0 left-0 w-full h-screen bg-white z-50 flex items-center justify-start flex-col py-32'
    >
      <button
        className='w-16 h-16 rounded-full flex items-center justify-center mb-24 hover:bg-zinc-50 duration-200'
        onClick={() => setOpenSearch(false)}
      >
        <span className='text-4xl text-orange-400'>
          <MdClose />
        </span>
      </button>
      <p className='text-3xl font-medium mb-12'>Search</p>

      <div className='w-3/5 mx-auto mb-12 grid grid-cols-4 gap-6'>
        {isLoading ? (
          <div className='col-span-4 flex items-center justify-center'>
            <p>Loading...</p>
          </div>
        ) : (
          data.map((category: CategoryTypes) => (
            <button className='py-3 text-base' key={category.id}>
              {category.name}
            </button>
          ))
        )}
      </div>

      <div className='w-4/5 mx-auto relative'>
        <input
          className='border-2 p-3 w-full text-base rounded-xl placeholder:text-zinc-300 border-zinc-100 '
          type='text'
          placeholder='Search for products'
          name='email'
          // value={values.email}
          // onChange={handleChange}
        />
        <span className='text-xl text-zinc-700 absolute top-2/4 right-6 -translate-y-2/4'>
          <BsSearch />
        </span>
      </div>
    </motion.div>
  );
};

export default SearchModal;
