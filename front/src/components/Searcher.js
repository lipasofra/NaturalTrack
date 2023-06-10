import TextField from "@mui/material/TextField";
import Button from '@mui/material/Button';

const Searcher = (props) => {

    
  return (
    <>
      <svg
        role="img"
        height="32"
        width="32"
        aria-hidden="true"
        viewBox="0 0 16 16"
        data-encore-id="icon"
        style={{ marginRight: "10px" }}
      >
        <path d="M7 1.75a5.25 5.25 0 1 0 0 10.5 5.25 5.25 0 0 0 0-10.5zM.25 7a6.75 6.75 0 1 1 12.096 4.12l3.184 3.185a.75.75 0 1 1-1.06 1.06L11.304 12.2A6.75 6.75 0 0 1 .25 7z"></path>
      </svg>
      <TextField
        id="searcher-text"
        // label="ej: Incendios en ..."
        variant="filled"
        type="text"
        style={{ width: "400px" }}
        // value={props.prompt}
        onChange={props.handlePromptChange}
      />
      <Button variant="text" style={{color:"white"}} onClick={props.sendPost}>Buscar</Button>
    </>
  );
};

export default Searcher