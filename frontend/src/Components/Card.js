import "../Components/Card.css";
import DeleteButton from "./Buttons";
function Card(props) {
  return (
    <div className="Card">
      <div>
        <p className ="listing_name">{props.name}Lorem ipsum dolor sit amet</p>
        <p className ="price">Price: {props.price}</p>
        <p className ="contact_info">Contact: {props.contact}</p>
      </div>
      <p>{props.desc}Description: Lorem ipsum dolor sit amet. Qui aperiam saepe qui natus voluptas et sunt dolorem ea aspernatur consequatur sed quia ducimus aut exercitationem omnis. Eum reiciendis aliquam sit blanditiis libero est quos dicta quo enim nesciunt ab saepe nihil. Et assumenda quos qui maxime alias cum incidunt quod alias repellat.</p>
      <DeleteButton />
    </div>
  );
}

export default Card;
