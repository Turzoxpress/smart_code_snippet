import CodeList from "./components/codelist";
import data from "./data.json"

function App() {
  return (
    <div>
      <CodeList data={data}/>
    </div>
  );
}

export default App;
