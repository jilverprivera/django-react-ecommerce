import { createContext, useState } from "react";
import { childrenProps } from "../types/layout";
import { LayoutContextTypes } from "../types/layoutContext";

export const LayoutContext = createContext({} as LayoutContextTypes);

export const LayoutContextProvider = ({ children }: childrenProps) => {
  const [menuOpen, setMenuOpen] = useState<boolean>(false);
  const [openFlyout, setOpenFlyout] = useState<boolean>(false);
  const [openSearch, setOpenSearch] = useState<boolean>(false);
  const [categorySearch, setCategorySearch] = useState<number | null>(1);
  const [productSelected, setProductSelected] = useState<number | null>(null);
  

  const state = {
    menuOpen,
    openSearch,
    openFlyout,
    categorySearch,
    productSelected,
    setMenuOpen,
    setOpenFlyout,
    setOpenSearch,
    setCategorySearch,
    setProductSelected
  };
  return (
    <LayoutContext.Provider value={state}>{children}</LayoutContext.Provider>
  );
};
