export type CategoryTypes = {
  id: number;
  name: string;
  slug: string;
  created_at: string;
  updated_at: string;
};

export type SubCategoryTypes = {
  id: number;
  name: string;
  slug: string;
  principal: CategoryTypes;
  created_at: string;
  updated_at: string;
};

export type ProductTypes = {
  id: number;
  title: string;
  slug: string;
  description: string;
  category: SubCategoryTypes;
  stars: number;
  total_stars: number;
  comment: Comment[];
  price: string;
  stock: number;
  sold: number;
  image: string;
  thumbnail: string;
  created_at: string;
  updated_at: string;
};

export type Comment = {
  created_at: string;
  updated_at: string;
  user: string;
  message: string;
};
