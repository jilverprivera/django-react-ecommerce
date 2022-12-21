export type LayoutContextTypes = {
  menuOpen: boolean;
  openFlyout: boolean;
  openSearch: boolean;

  setOpenFlyout: (arg: boolean) => void;
  setMenuOpen: (arg: boolean) => void;
  setOpenSearch: (arg: boolean) => void;
};
