import "./Navbar.css";
import goosepic from "../Assets/goose.jpg";
function Navbar() {
  return (
    <div className="nav">
      <img className="gooseimage" src={goosepic} alt="" />
      <h1 className="header-title">Geese Migration</h1>
      <button className ="header-button">+ Add Listing</button>
    </div>
  );
}

export default Navbar;
