import { Navigate } from "react-router-dom";

type Props = {
  component: React.ComponentType;
  path?: string;
  roles?: Array<string>;
};

export const PublicRoute = ({ component: RouteComponent }: Props) => {
  const isLogged = false;
  if (!isLogged) {
    return <RouteComponent />;
  }

  if (!isLogged) {
    return <div>Don't have permissions</div>;
  }

  return <Navigate to='/' />;
};
