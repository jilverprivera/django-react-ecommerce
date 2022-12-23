import CategoryDivider from "../components/CategoryDivider";

import Container from "../layout/Container";

const Home = () => {
  return (
    <Container title='Home - Ecommerce'>
      {/* <PageBanner path={pathname} /> */}
      <section className='max-w-screen-2xl w-full mx-auto py-32'>

        <div className="pt-24">

        <CategoryDivider />
        </div>
      </section>
    </Container>
  );
};

export default Home;
