import "./Navbar.css";
import goosepic from "../Assets/goose.jpg";
import AddListingButton from "./AddListingButton";
function Navbar(props) {
  return (
    <div className="nav1">
      <img className="gooseimage" src={goosepic} alt="" />
      <h1 className="header-title">Geese Migration</h1>
      <AddListingButton add_item={props.add_list} />
    </div>
  );
}

export default Navbar;
