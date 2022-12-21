import { Navigate } from "react-router-dom";

type Props = {
  component: React.ComponentType;
  path?: string;
  roles: Array<string>;
};

export const PublicRoute = ({ component: RouteComponent }: Props) => {
  // get from context
  const isLogged = true;
  const userHasRequiredRole = true;
  if (!isLogged && !userHasRequiredRole) {
    return <RouteComponent />;
  }

  if (!isLogged && !userHasRequiredRole) {
    return <div>Don't have permissions</div>;
  }

  return <Navigate to='/' />;
};
