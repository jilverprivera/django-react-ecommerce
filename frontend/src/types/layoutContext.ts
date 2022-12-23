export type LayoutContextTypes = {
  menuOpen: boolean;
  openFlyout: boolean;
  openSearch: boolean;
  categorySearch: number | null;
  productSelected: number | null;

  setOpenFlyout: (arg: boolean) => void;
  setMenuOpen: (arg: boolean) => void;
  setOpenSearch: (arg: boolean) => void;
  setCategorySearch: (arg: number) => void;
  setProductSelected: (arg: number | null) => void;
};
