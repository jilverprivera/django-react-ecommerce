import React from "react";

const CategoryDivider = () => {
  return (
    <div className='w-full grid grid-cols-2 grid-rows-6 gap-6'>
      <div className='w-full rounded-md p-6 aspect-square border-2 col-start-1 row-start-1'></div>
      <div className='w-full rounded-md p-6 border-2 col-start-2 row-start-1 row-span-2'></div>
      <div className='w-full rounded-md p-6 border-2 col-start-1 row-start-2 row-span-2'></div>
      <div className='w-full rounded-md p-6 border-2 col-start-2 row-start-3 row-span-2'></div>
      <div className='w-full rounded-md p-6 border-2 col-start-1 row-start-4 row-span-2'></div>
      <div className='w-full rounded-md p-6 aspect-square border-2 col-start-2 row-start-5'></div>
    </div>
  );
};

export default CategoryDivider;
