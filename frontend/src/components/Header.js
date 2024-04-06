import { Link } from "react-router-dom";
import { useState, useRef } from "react";
// import workerUrl from "./worker.js";

function Header() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [hoveredItem, setHoveredItem] = useState(1);
  // const pageStore = usePageStore();
  // const worker = new Worker(new URL("./worker.js", import.meta.url));
  // pageStore.setWorker(worker);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  const closeMobileMenu = () => {
    setIsMobileMenuOpen(false);
  };

  const handleHover = (item) => {
    setHoveredItem(item);
  };

  return (
    <header className="bg-white border-b border-gray-300 z-10">
      <div className="container mx-auto bg-fixed max-w-5xl py-4 px-8">
        <div className="flex justify-between">
          <span className="flex items-center">
            <Link to="/" className="pr-1">
              <svg
                version="1.0"
                width="30"
                height="30pt"
                viewBox="0 0 190 184.2"
                preserveAspectRatio="xMidYMid meet"
                xmlns="http://www.w3.org/2000/svg"
              >
                {/* SVG path here */}
              </svg>
            </Link>
            <span className="text-xl font-bold">DMI Finance</span>
          </span>

          <div className="hidden sm:flex items-center justify-between px-2">
            <nav>
              {/* <Link to="/" className="text-black hover:text-blue-600">
                Home
              </Link>
              &nbsp;
              <Link to="/blo" className="text-black hover:text-blue-600">
                Blog
              </Link>
              &nbsp;
              <Link to="/help" className="text-black hover:text-blue-600">
                Help
              </Link>
              &nbsp; */}
            </nav>

            <div className="flex items-center justify-between">
              {/* <Link to="/login" className="text-black hover:text-blue-600 px-2">
                Login
              </Link>
              &nbsp;
              <Link to="/register">
                <button className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                  Register
                </button>
              </Link> */}
            </div>
          </div>
          <button
            className="block sm:hidden p-1 m-1 rounded focus:outline-none hover:bg-gray-100 group"
            onClick={toggleMobileMenu}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              className="w-6 h-6"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
                />
              </svg>
            </svg>
          </button>

          {/* Mobile menu */}
          {isMobileMenuOpen && (
            <div className="sm:hidden" role="dialog" aria-modal="true">
              {/* Background backdrop */}
              <div
                className="fixed inset-0 z-10"
                onClick={closeMobileMenu}
              ></div>

              <div className="fixed inset-y-0 right-0 z-10 w-1/2 shadow-xl overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10 mx-auto">
                <div className="flex justify-end">
                  <button
                    type="button"
                    className="-m-2.5 rounded-md p-2.5 text-gray-700"
                    onClick={closeMobileMenu}
                  >
                    <span className="sr-only">Close menu</span>
                    <svg
                      className="h-6 w-6"
                      fill="none"
                      viewBox="0 0 24 24"
                      strokeWidth="1.5"
                      stroke="currentColor"
                      aria-hidden="true"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        class="w-6 h-6"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          d="M6 18 18 6M6 6l12 12"
                        />
                      </svg>
                    </svg>
                  </button>
                </div>
                <div className="mt-6 flow-root">
                  <div className="-my-6 divide-y divide-gray-500/10">
                    <div className="space-y-2 py-6">
                      <Link
                        to="/"
                        className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50 hover:text-blue-700"
                        onClick={closeMobileMenu}
                      >
                        Home
                      </Link>
                      <Link
                        to="/blo"
                        className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50 hover:text-blue-700"
                        onClick={closeMobileMenu}
                      >
                        Blog
                      </Link>
                      <Link
                        to="/help"
                        className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50 hover:text-blue-700"
                        onClick={closeMobileMenu}
                      >
                        Help
                      </Link>
                      &nbsp;
                    </div>
                    <div className="space-y-2 py-6">
                      <Link
                        to="/login"
                        className="-mx-3 block rounded-lg px-3 py-2.5 text-base text-center font-semibold leading-7 bg-blue-200 text-gray-900"
                        onClick={() => handleHover(1)}
                        onMouseLeave={() => handleHover(0)}
                      >
                        Log in
                      </Link>
                      <Link
                        to="/register"
                        className="-mx-3 block rounded-lg px-3 py-2.5 text-base text-center font-semibold leading-7 text-gray-900 bg-blue-200"
                        onClick={() => handleHover(2)}
                        onMouseLeave={() => handleHover(0)}
                      >
                        Register
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}

export default Header;
