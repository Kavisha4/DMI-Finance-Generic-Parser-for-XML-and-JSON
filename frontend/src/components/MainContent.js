import React, { useState } from "react";

const MainContent = () => {
  const [xmlInput, setXmlInput] = useState("");
  const [jsonInput, setJsonInput] = useState("");
  const [metadata, setMetadata] = useState("");
  const [output, setOutput] = useState("");

  // Function to parse XML input
  const parseXml = () => {
    // Parse XML logic goes here
    try {
      // Example: Parsing XML using DOMParser
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(xmlInput, "text/xml");
      setOutput(xmlDoc.documentElement.outerHTML);
    } catch (error) {
      setOutput("Error parsing XML");
    }
  };

  // Function to parse JSON input
  const parseJson = () => {
    // Parse JSON logic goes here
    try {
      const jsonData = JSON.parse(jsonInput);
      setOutput(JSON.stringify(jsonData, null, 2));
    } catch (error) {
      setOutput("Error parsing JSON");
    }
  };

  return (
    <>
      <div className="flex flex-col border">
        <div className="flex">
          <label>XML Input:</label>
          <textarea
            value={xmlInput}
            onChange={(e) => setXmlInput(e.target.value)}
            rows={5}
            cols={50}
            className="border"
          />
        </div>
        <div>
          <label>JSON Input:</label>
          <textarea
            value={jsonInput}
            onChange={(e) => setJsonInput(e.target.value)}
            rows={5}
            cols={50}
            className="border"
          />
        </div>
        <div>
          <label>Metadata:</label>
          <input
            type="text"
            value={metadata}
            onChange={(e) => setMetadata(e.target.value)}
            className="border"
          />
        </div>
        <button onClick={parseXml}>Parse XML</button>
        <button onClick={parseJson}>Parse JSON</button>
        <div>
          <h3>Output:</h3>
          <textarea
            value={output}
            readOnly
            rows={10}
            cols={50}
            className="border"
          />
        </div>
      </div>
    </>
  );
};

export default MainContent;
