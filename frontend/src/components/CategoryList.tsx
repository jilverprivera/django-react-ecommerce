import { useContext } from "react";
import { LayoutContext } from "../context/LayoutContext";
import { useData } from "../hooks/useData";
import { CategoryTypes } from "../types";

const CategoryList = () => {
  const { setCategorySearch, categorySearch } = useContext(LayoutContext);

  const { data } = useData("http://127.0.0.1:8000/api/categories/");
  return (
    <div className='w-full flex items-start justify-center flex-col'>
      {data &&
        data
          .sort((a: CategoryTypes, b: CategoryTypes) =>
            a.created_at.localeCompare(b.created_at)
          )
          .map((category: CategoryTypes) => (
            <button
              className={`${
                categorySearch === category.id ? "font-medium" : "font-normal"
              } my-3 text-base hover:font-medium`}
              key={category.id}
              onClick={() => setCategorySearch(category.id)}
            >
              {category.name}
            </button>
          ))}
    </div>
  );
};

export default CategoryList;
