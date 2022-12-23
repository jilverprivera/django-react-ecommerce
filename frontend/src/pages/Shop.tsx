import Category from "../components/Category";
import Products from "../components/Products";
import {useState} from "react"
import Container from "../layout/Container";
import { CiGrid2H, CiGrid41 } from "react-icons/ci";
import { BsSearch } from "react-icons/bs";

const Shop = () => {
  return (
    <Container title='Shop - Ecommerce'>
      <section className='max-w-screen-2xl w-11/12 mx-auto pt-48'>
        <div className='grid grid-cols-5 gap-12 py-12'>
          <div>
            <div className="h-12 flex items-center justify-start mb-6">

            <h2 className='w-ful<l text-2xl'>Categories</h2>
            </div>
            <Category />
          </div>
          <div className='w-full col-span-4'>
            <div className='w-full col-span-4 grid grid-cols-3 gap-6 mb-6'>
              <div className='col-span-2 relative'>
                <input
                  className='w-full border-2 rounded-md h-full px-3'
                  type='text'
                  placeholder='Search...'
                />
                <span className='absolute top-2/4 -translate-y-2/4 right-3'>
                  <BsSearch />
                </span>
              </div>
              <div className=' flex items-center justify-end'>
                <button className='h-12 w-12 flex items-center justify-center text-2xl border-2 border-stone-100 rounded-md '>
                  <CiGrid41 />
                </button>
                <button className='h-12 w-12 flex items-center justify-center text-2xl border-2 border-stone-100 rounded-md ml-3'>
                  <CiGrid2H />
                </button>
              </div>
            </div>
            <Products />
          </div>
        </div>
      </section>
    </Container>
  );
};

export default Shop;
