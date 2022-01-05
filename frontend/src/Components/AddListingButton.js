import "./AddListingButton.css";
import { useState } from "react";
import Modal from "react-bootstrap/Modal";
function AddListingButton(props) {
  // Use state hooks
  const [listing_name,setLising_name] = useState("");
  const [price,setPrice] = useState("");
  const [contact,setContact] = useState("");
  const [location,setLocation] = useState("");
  const [description,setDescription] = useState("");

  
  const [show, setShow] = useState(false);
  const handleClose = () => {
    setLising_name("");
    setPrice("");
    setContact("");
    setLocation("");
    setDescription("");
    setShow(false)
  };
  const handleShow = () => {
    setLising_name("");
    setPrice("");
    setContact("");
    setLocation("");
    setDescription("");
    setShow(true)
  };

  const handleAddListing = () => {
    props.add_item(listing_name, price, contact, location, description);
    setLising_name("");
    setPrice("");
    setContact("");
    setLocation("");
    setDescription("");
    setShow(false);
  };

  const changeListingName = (e) =>{
    setLising_name(e.target.value);
  }
  const changePrice = (e) => {
    setPrice(e.target.value);
  }
  const changeLocation = (e) => {
    setLocation(e.target.value);
  }
  const changeContact = (e) => {
    setContact(e.target.value);
  }
  const changeDescription = (e) =>{
    setDescription(e.target.value);
  }
  return (
    <>
      <button className="header-button" onClick={handleShow}>
        + Add Listing
      </button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Add Listing</Modal.Title>
        </Modal.Header>
        
        <Modal.Body>Add your listing information
        <div class="modal-body">
        <form>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Listing Name:</label>
            <input type="text" class="form-control" id="recipient-name" value = {listing_name} onChange ={changeListingName}/>
          </div>

          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Price (CAD)</label>
            <input type="text" class="form-control" id="recipient-name"  value = {price} onChange ={changePrice}/>
          </div>

          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Location</label>
            <input type="text" class="form-control" id="recipient-name" value = {location} onChange ={changeLocation}/>
          </div>

          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Contact Info</label>
            <input type="text" class="form-control" id="recipient-name" value = {contact} onChange ={changeContact}/>
          </div>


          <div class="form-group">
            <label for="message-text" class="col-form-label">Description:</label>
            <textarea class="form-control" id="message-text" value = {description} onChange = {changeDescription}></textarea>
          </div>
        </form>
      </div>
        </Modal.Body>

        <Modal.Footer>
          <button variant="secondary" onClick={handleClose}>
            Cancel
          </button>
          <button variant="primary" onClick={handleAddListing}>
            Create Listing
          </button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default AddListingButton;
