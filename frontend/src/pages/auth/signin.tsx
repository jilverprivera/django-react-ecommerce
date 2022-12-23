import { Link } from "react-router-dom";
import { MdArrowBackIosNew } from "react-icons/md";

import Container from "../../layout/Container";
import { useForm } from "../../hooks/useForm";

const SignIn = () => {
  const { values, handleChange } = useForm({
    email: "",
    password: "",
  });
  const handleSignIn = async (e: any) => {
    e.preventDefault();
  };

  return (
    <Container title='Sign In - TechCommerce'>
      <section className='w-full h-screen relative'>
        <div className='absolute bg-zinc-800 top-0 left-0 w-2/4 h-screen'>
          <div className='relative w-full h-full'>
            <div className='absolute top-12 left-16'>
              <Link to='/' className='flex items-center justify-center'>
                <span className='text-zinc-50 text-3xl'>
                  <MdArrowBackIosNew />
                </span>
                <span className='text-zinc-50 text-lg ml-3'>Back</span>
              </Link>
            </div>
          </div>
        </div>

        <div className='absolute bg-white top-0 right-0 w-2/4 h-screen px-24 py-12'>
          <div className='w-full h-full relative'>
            <div className='flex items-center justify-center absolute top-0 right-0'>
              <p className='text-base font-medium tracking-wider text-zinc-700 mr-6'>
                Don&apos;t have account yet?
              </p>
              <Link
                to='/signup'
                className='px-6 py-3 rounded-3xl uppercase text-zinc-50 font-semibold tracking-wider bg-gradient-to-br from-sky-600 via-blue-600 to-violet-700'
              >
                Sign Up
              </Link>
            </div>
            <div className='pt-24'>
              <div className='mb-12'>
                <h1 className='text-5xl font-bold text-zinc-900 mb-3'>
                  Welcome back!
                </h1>
                <span className='text-xl font-semibold text-zinc-600'>
                  Let&apos;s buy something
                </span>
              </div>

              <form
                className='w-full flex items-start justify-center flex-col'
                onSubmit={handleSignIn}
              >
                <div className='w-4/5 mb-6'>
                  <label htmlFor='name' className='text-lg font-medium'>
                    Email
                  </label>
                  <input
                    className='border-2 p-3 w-full text-lg rounded-xl placeholder:text-zinc-200 border-zinc-200 mt-1.5'
                    type='text'
                    placeholder='example: faketest@gmail.com'
                    name='email'
                    value={values.email}
                    onChange={handleChange}
                  />
                </div>
                <div className='w-4/5 mb-12'>
                  <label htmlFor='name' className='text-lg font-medium'>
                    Password
                  </label>
                  <input
                    className='border-2 p-3 w-full text-lg rounded-xl placeholder:text-zinc-200 border-zinc-200 mt-1.5'
                    type='password'
                    placeholder='6+ characters'
                    name='password'
                    value={values.password}
                    onChange={handleChange}
                  />
                </div>
                <button
                  type='submit'
                  className='py-3 rounded-xl w-4/5 font-medium text-lg text-zinc-50 bg-gradient-to-br from-sky-600 via-blue-600 to-violet-700'
                >
                  Sign In
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>
    </Container>
  );
};

export default SignIn;
