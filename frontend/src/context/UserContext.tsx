import { createContext, useState } from "react";
import { UserContextTypes } from "../types/userContext";
import { childrenProps } from "../types/layout";

export const UserContext = createContext({} as UserContextTypes);

export const UserContextProvider = ({ children }: childrenProps) => {
  const [isLogged] = useState<boolean>(false);
  const [isAdmin] = useState<boolean>(false);
  const [token] = useState<string>("");

  const state = {
    isLogged,
    isAdmin,
    token,
  };
  return <UserContext.Provider value={state}>{children}</UserContext.Provider>;
};
