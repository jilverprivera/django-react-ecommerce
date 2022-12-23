type props = {
  path: string;
};
const PageBanner = ({ path }: props) => {
  const route = path.replace("/", " ");

  return (
    <section className='w-full h-[32rem] relative top-0 left-0 flex items-center justify-center bg-zinc-50'>
      <span>Home</span>
      {path !== "/" && <span className="mx-1.5">/</span>}
      <span className="font-semibold">{route}</span>
    </section>
  );
};

export default PageBanner;
