import "./App.css";
import Container from "./Components/Container.js";
import Navbar from "./Components/Navbar.js";
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [houses, setHouses] = useState([]);

  const get_houses = () => {
    axios.get("http://127.0.0.1:5000/").then((response) => {
      let listings = JSON.parse(response.data);
      console.log(listings);
      setHouses(listings);
    });
  };

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/").then((response) => {
      let listings = JSON.parse(response.data);
      setHouses(listings);
    });
  }, []);

  const delete_list = async (id1) => {
    console.log(id1);
    console.log("passed");
    await axios.post("http://127.0.0.1:5000/delete", { id: id1 });
    get_houses();
  };

  const add_list = async (listName, priceIn, contactIn, descIn, locationIn) => {
    await axios.post("http://127.0.0.1:5000/add", {
      listing_name: listName,
      price: priceIn,
      contact: contactIn,
      description: descIn,
      location: locationIn,
      image: "",
    });
    get_houses();
  };

  return (
    <div className="background">
      <Navbar add_list={add_list} />
      <br />
      <Container houses={houses} delete_list={delete_list} />
    </div>
  );
}

export default App;
