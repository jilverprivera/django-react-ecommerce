export const getProducts = async () => {
  const response = await fetch("http://127.0.0.1:8000/api/products/");
  const data = await response.json();
  return data;
};
