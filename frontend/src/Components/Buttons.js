import "./Button.css";

function DeleteButton(props) {
  let id = props.id;
  const deletelist = () => {
    props.deleteListing(id);
  };
  return (
    <button className="DeleteButton" onClick={deletelist}>
      Delete
    </button>
  );
}
export default DeleteButton;
