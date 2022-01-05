import "./Container.css";
import Card from "./Card.js";
function Container(props) {
  let houses = props.houses;
  return (
    <div className="Container">
      {houses.map((house) => (
        <Card house={house} delete_list={props.delete_list} />
      ))}
    </div>
  );
}

export default Container;
