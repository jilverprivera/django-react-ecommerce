import { createContext, useState } from "react";
import { AppContextProps } from "../types/context";
import { childrenProps } from "../types/layout";

export const Context = createContext({} as AppContextProps);

export const ContextProvider = ({ children }: childrenProps) => {
  const [menuOpen, setMenuOpen] = useState<boolean>(false);
  const [searchModal, setSearchModal] = useState<boolean>(false);

  const [isLogged, setIsLogged] = useState<boolean>(false);
  const [isAdmin, setIsAdmin] = useState<boolean>(false);
  const [token, setToken] = useState<string>("");

  const state = {
    menuOpen,
    searchModal,
    isLogged,
    isAdmin,
    token,
    setMenuOpen,
    setSearchModal,
  };
  return <Context.Provider value={state}>{children}</Context.Provider>;
};
