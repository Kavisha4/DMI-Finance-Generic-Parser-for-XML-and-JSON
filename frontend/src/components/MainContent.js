import React, { useState } from "react";

const MainContent = () => {
  const [jsonInput, setJsonInput] = useState("");
  const [metadata, setMetadata] = useState("");
  const [output, setOutput] = useState("");

  // Function to parse JSON input
  const parseJson = async () => {
    try {
      const response = await fetch(
        "https://dmi-finance-generic-parser-for-xml-and-json-8q3hrvmal.vercel.app/",
        {
          mode: "no-cors",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: jsonInput,
        }
      );
      const data = await response.text();
      setOutput(data);
    } catch (error) {
      setOutput("Error parsing JSON");
    }
  };

  return (
    <>
      <div className="flex flex-col border p-4 space-y-4 min-h-screen">
        <div className="flex items-center font-bold">
          <label className="mr-2">JSON Input:</label>
          <textarea
            value={jsonInput}
            onChange={(e) => setJsonInput(e.target.value)}
            rows={5}
            cols={50}
            className="border-2 border-black p-2 flex-1 m-2 rounded-lg"
          />
        </div>
        <div className="flex items-center font-bold">
          <label className="mr-2">Metadata:</label>
          <input
            type="text"
            value={metadata}
            onChange={(e) => setMetadata(e.target.value)}
            className="border-2 border-black p-2 flex-1 rounded-lg"
          />
        </div>

        <button
          onClick={parseJson}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Parse JSON
        </button>
        <div className="border border-black rounded-lg">
          <h3 className="p-2 font-bold">Output:</h3>
          <textarea
            value={output}
            readOnly
            rows={5}
            className="borde p-2 flex-1 rounded-lg"
            style={{ width: "calc(100% - 16px)" }}
          />
        </div>
      </div>
    </>
  );
};

export default MainContent;
