import { useContext } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { BsFillBagFill, BsFillStarFill, BsHeartFill } from "react-icons/bs";
import { Link } from "react-router-dom";

import { LayoutContext } from "../context/LayoutContext";

import { ProductTypes } from "../types";

const ProductCard = ({
  id,
  thumbnail,
  title,
  price,
  stars,
  description,
  slug,
}: ProductTypes) => {
  const { productSelected, setProductSelected } = useContext(LayoutContext);
  const product_stars = new Array(stars).fill(" ");

  return (
    <Link
      to={slug}
      className='w-full rounded-xl overflow-hidden bg-white border-2 border-zinc-100 relative'
      onMouseEnter={() => setProductSelected(id)}
      onMouseLeave={() => setProductSelected(null)}
    >
      <div className='w-full relative'>
        <AnimatePresence exitBeforeEnter>
          {productSelected === id && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.25 }}
              className='absolute bottom-3 right-3 bg-white'
            >
              <div className='w-12 h-12 flex items-center justify-center border-2 rounded-md mb-1.5'>
                <BsHeartFill />
              </div>
              <div className='w-12 h-12 flex items-center justify-center border-2 rounded-md'>
                <span className="text-xl">
                  <BsFillBagFill />
                </span>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        <img
          src={thumbnail}
          alt={title}
          className='w-full aspect-square object-contain'
        />
      </div>
      <div className='w-full p-6'>
        <p className='text-lg font-medium'>{title}</p>
        <p className='text-sm font-normal leading-relaxed my-3'>
          {description}
        </p>
        <div className='w-full flex items-center justify-between'>
          <p className=''>$ {price}</p>
          <div className='flex items-center justify-start'>
            {product_stars.map((star, i) => (
              <span className='text-yellow-400 mr-1.5 last:mr-0'>
                <BsFillStarFill />
              </span>
            ))}
          </div>
        </div>
      </div>
    </Link>
  );
};

export default ProductCard;
