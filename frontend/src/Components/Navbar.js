import "./Navbar.css";
import goosepic from "../Assets/goose.jpg";
import AddListingButton from "./AddListingButton";
function Navbar() {
  return (
    <div className="nav">
      <img className="gooseimage" src={goosepic} alt="" />
      <h1 className="header-title">Geese Migration</h1>
      <button className="header-button1">+ Add Listing</button>
      {
        //<AddListingButton />
      }
    </div>
  );
}

export default Navbar;
