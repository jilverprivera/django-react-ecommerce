import { useState } from "react";
import { useData } from "../hooks/useData";
import { CategoryTypes } from "../types";
import Accordion from "./AccordionLayout";

const Category = () => {
  const [category, setCategory] = useState<CategoryTypes>({
    id: 1,
    name: "All",
    slug: "all",
    created_at: "",
    updated_at: "",
  });
  const [activeCategory, setActiveCategory] = useState<number | null>(null);

  const { data: categories, isLoading: categoriesLoading } = useData(
    "http://127.0.0.1:8000/api/categories/"
  );

  return (
    <div>
      {categoriesLoading ? (
        <p>Loading...</p>
      ) : (
        categories
          .sort((a: CategoryTypes, b: CategoryTypes) =>
            a.created_at.localeCompare(b.created_at)
          )
          .map((category: CategoryTypes) => (
            <Accordion
              key={category.id}
              category={category}
              activeCategory={activeCategory}
              setActiveCategory={setActiveCategory}
            />
          ))
      )}
    </div>
  );
};

export default Category;
