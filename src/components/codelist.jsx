import { useState } from "react";
import copy from "copy-to-clipboard";
// ES6 Modules or TypeScript
import Swal from "sweetalert2";

const CodeList = ({ data }) => {
  const [selectedFilePath, setSelectedFilePath] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [fileContents, setFileContents] = useState(null);
  const [copySuccess, setCopySuccess] = useState(false);

  const handleViewFileClick = (filePath) => {
    setSelectedFilePath(filePath);
    fetchFileContents(filePath);
  };

  const handleCopyClick = () => {
    copy(fileContents);
    setCopySuccess(true);

    Swal.fire({
      position: "middle",
      icon: "success",
      title: "Copied Successfully!",
      showConfirmButton: false,
      timer: 1500,
    });
  };

  const fetchFileContents = async (filePath) => {
    try {
      const response = await fetch(filePath);
      const text = await response.text();
      setFileContents(text);
    } catch (error) {
      console.error(error);
    }
  };

  const filteredData = data.filter((item) =>
    item.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="w-full md:w-2/3 mx-auto">
      <div className="mb-4 ">
        <input
          type="text"
          placeholder="Binary Sort"
          className="w-full px-4 py-2 mt-[50px] rounded-md shadow-md border focus:outline-[#b9b5b5] border-[#cbc5c5]"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredData.map((item, index) => (
          <div
            key={index}
            className="flex flex-col items-center p-4 rounded-lg shadow-md"
          >
            <div className="flex-1">{item.title}</div>
            <button
              className="mt-4 px-4 py-2 text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none"
              onClick={() => handleViewFileClick(item.filePath)}
            >
              View Code
            </button>
          </div>
        ))}
      </div>
      {selectedFilePath && (
        <div className="fixed top-0 left-0 right-0 bottom-0 z-10 flex items-center justify-center bg-black bg-opacity-50">
          <div className="bg-white p-6 rounded-lg shadow-md max-w-full max-h-full overflow-auto xl:w-3/5 lg:w-3/5 md:w-4/5 sm:w-11/12">
            <div className="mb-2 font-bold">File Path:</div>
            <div className="bg-white p-2 rounded-lg mb-4">
              {selectedFilePath}
            </div>
            <div className="h-96 overflow-y-scroll">
              <pre className="p-4 bg-gray-900 text-white rounded-lg">
                {fileContents}
              </pre>
            </div>
            <div className="flex justify-end mt-4">
              <button
                className="mr-4 px-4 py-2 text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none"
                onClick={handleCopyClick}
              >
                Copy
              </button>
              <button
                className="px-4 py-2 text-white bg-gray-500 rounded-lg hover:bg-gray-600 focus:outline-none"
                onClick={() => {
                  setSelectedFilePath(null);
                  setFileContents(null);
                }}
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default CodeList;
