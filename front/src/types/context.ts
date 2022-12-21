export type AppContextProps = {
  menuOpen: boolean;
  searchModal: boolean;
  isAdmin: boolean;
  isLogged: boolean;
  token: string;

  setMenuOpen: (arg: boolean) => void;
  setSearchModal: (arg: boolean) => void;
};
