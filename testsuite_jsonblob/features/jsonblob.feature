Feature: JsonBlob API
  Scenario Outline: Create new blog post
    Examples:
     | body                                     | expected_status |
     | {"apple":5}                              | 201             |
     | unvalid                                  | 400             |
     | {"names":["Joe","Hilary","Peter"]}       | 201             |

  Given a testable API
  When post request is received on endpoint with <body>
  Then <expected_status> is responded
  And in the response blobId is found

#TODO it could be solved nicer with storing created ids and the update and delete could pick from there
  Scenario Outline: Update the blog post
    Examples:
     |body                                | update_to_body                            | expected_status |
     | {"apple":5}                        | {"peach":15}                              | 200             |
     | unvalid                            | unvalid input 2                           | 404             |
     | {"names":["Joe","Hilary","Peter"]} | {"names":["Joe","Hilary","Peter"]}        | 200             |

  Given a testable API
  When post request is received on endpoint with <body>
  And in the response blobId is found
  And put request is received on endpoint/blobId with <update_to_body>
  Then <expected_status> is responded


  Scenario Outline: Delete the blog post
    Examples:
     | body                               | expected_status |
     | {"apple":5}                        | 200             |
     | unvalid                            | 500             |
     | {"names":["Joe","Hilary","Peter"]} | 200             |

  Given a testable API
  When post request is received on endpoint with <body>
  And in the response blobId is found
  And delete request is received on endpoint/blobId
  Then <expected_status> is responded
