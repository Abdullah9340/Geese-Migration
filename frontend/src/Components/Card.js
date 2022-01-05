import "../Components/Card.css";
import DeleteButton from "./Buttons";
function Card(props) {
  return (
    <div className="Card">
      <div>
        <p className="listing_name">{props.house.listing_name}</p>
        <p className="price">Price (CAD): {props.house.price}</p>
        <p className="contact_info">
          {props.house.id === -1 && <a href={props.house.link}>Contact</a>}
          {props.house.id !== -1 && <p>Contact: {props.house.link}</p>}
        </p>
      </div>
      <p>{props.house.desc}</p>
      {props.house.id !== -1 && (
        <DeleteButton deleteListing={props.delete_list} id={props.house.id} />
      )}
    </div>
  );
}

export default Card;
